/*
    This code uses GSL to calculate the fourier transform of sinc function and
    then plot it along with the analytical fourier transformed function.
*/

#include <stdio.h>
#include <math.h>
#include <gsl/gsl_fft_complex.h>
#include <complex.h>

#define REAL(z,i) ((z)[2*(i)])     // Accessing real part of the array z
#define IMAG(z,i) ((z)[2*(i)+1])   // Accessing imaginary part of the array z

// Defining sinc function
double sinc(double x) {
    if (x == 0.0) {
        return 1.0;
    } else {
        return sin(x) / x;
    }
}

// Defining analytical fourier transform of sinc function
double analytical_ft(double k, double pi){
    if(k<=1.0 && k>=-1.0){
       return sqrt(pi/2);
    }
    else{
       return 0.0;
    }
}

int main(){
    int n = 1024; // No. of sample points
    double Pi = acos(-1.0);
    double f[2*n],k[n],factor;

    // Defining x range
    double xmin = -50.;
    double xmax = 50.;
    double dx = (xmax - xmin)/n;
    
    for (int i=0; i<n; ++i){      
         REAL(f,i)=sinc(xmin+i*dx);  
         IMAG(f,i)=0.0;
    }

    gsl_fft_complex_radix2_forward(f, 1, n);  //Calculating Fourier Transform
  
    FILE *output_file1 = fopen("box1.dat", "w"); // For storing numerical FT
    FILE *output_file2 = fopen("box2.dat", "w"); // For storing analytical FT

    /*
         Since gsl returns the fourier transform of f(x) in out array with its first element value
         at k=0. Then it returns N/2-1 values with positive k values and then the remaining N/2 
         values of the fourier transformed function. Hence we need to adjust the values of k 
         accordingly. Moreover it returns a complex function with real components in the 2*i th
         element and imaginary values in the (2*i+1)th element.
    */
    for (int i=0; i<n; ++i){
         if (i==0){
             k[i] = 0;
         }
         else if (i<n/2){
             k[i] = i / (n * dx);
         }
         else {
             k[i] = -(n-i) / (n * dx);
         }
         // Calculating the factor properly such that the FFT is correctly normalized
         factor = dx * sqrt(1.0/(2*Pi)) * creal(cexp(I*k[i]*2*Pi*xmin));
         // k are multiplied by 2*pi to convert to angular frequency
         fprintf(output_file1, "%f %f\n", 2* Pi* k[i], factor*REAL(f,i));
         fprintf(output_file2, "%f %f\n", 2*Pi*k[i], analytical_ft(2*Pi*k[i], Pi));
    }
    fclose(output_file1);
    fclose(output_file2);
    return 0;
}


