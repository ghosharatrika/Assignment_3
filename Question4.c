/*
   This code uses FFTW to calculate the fourier transform of gaussian function 
   and plots it along with the analytical fourier transformed function
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#include <complex.h>

#define N 1024 // Number of samples

// Defining the gaussian function
double gaussian(double x){
    return exp(-x*x);
}

// Defining the analytical fourier transform of gaussian function
double analytical_ft(double k, double PI){
    return sqrt(0.5)* exp(-k*k/4.0);
}

int main() {
    int i;
    double x[N], k[N], f[N], delta_x, factor;
    fftw_complex *in, *out;
    fftw_plan p;
    
    // Defining Pi
    double PI = acos(-1.0);
    
    // Defining xmin, xmax
    double xmin = -10.0;
    double xmax = 10.0;
    delta_x = (xmax-xmin)/N;
    
    // Initializeing FFTW arrays
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    
    // Creating file that will store the data values of sinc function
    FILE *analytical_file = fopen("gauss_in.dat", "w"); 
    for (i = 0; i < N; ++i) {
        x[i] = xmin + i * delta_x;
        fprintf(analytical_file, "%f %f\n", x[i], gaussian(x[i]));
        in[i][0] = gaussian(x[i]); // Real part of the function to be fourier transform
        in[i][1] = 0.0; // Imaginary part of the function to be fourier transform
    }
    fclose(analytical_file);
    
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE); // Creating plan
    // FFTW returns the fourier transform without any prefactor of 1/sqrt(n)
    
    fftw_execute(p); // Executing FFT

    FILE *output_file = fopen("gaussian.dat", "w"); // Writing output to a file ''box.dat''
    FILE *output_file2 = fopen("gaussian2.dat", "w"); // Writing analytical solution to a file ''box.2dat''
    
    /*
         Since FFTW returns the fourier transform of f(x) in out array with its first element value
         at k=0. Then it returns N/2-1 values with positive k values and then the remaining N/2 
         values of the fourier transformed function. Hence we need to adjust the values of k 
         accordingly 
    */
    for (i = 0; i < N; ++i) {
        if (i==0){
           k[i] = 0;
        }
        else if (i<N/2){
            k[i] = i / (N * delta_x);
        }
        else {
            k[i] = -(N-i) / (N * delta_x);
        }
        // Calculating the properly such that the FFT is correctly normalized
        factor = delta_x * sqrt(1.0/(2*PI)) * creal(cexp(I*k[i]*2*PI*xmin));
        // Multiplying k by 2*pi to convert to angular frequency
        fprintf(output_file, "%f %f\n", 2*PI*k[i], fabs(factor * out[i][0]));
        fprintf(output_file2, "%f %f\n", 2*PI*k[i], analytical_ft(2*PI*k[i],PI));
    }
    fclose(output_file);
    fclose(output_file2);
    
    // Clean up
    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return 0;
}

