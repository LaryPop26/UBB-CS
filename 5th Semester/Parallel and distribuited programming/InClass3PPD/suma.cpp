#include <iostream>
#include <stdio.h>
#include <mpi.h>

using namespace std;
const int N=10;

void print(int* a, int n) {
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}
int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);
    int a[N];
    int b[N];
    int c[N];
    MPI_Status status;

    int rank, size;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int dim = N / (size-1);
    if (rank==0) {
        for ( int i=0; i<N; ++i) {
            a[i] = rand() %10; //i
            b[i] = rand() %10; //i
        }
        int start = 0;
        int r = N % (size-1);
        int end = dim;
        auto startTime = MPI_Wtime();
        for ( int i=1; i < size; ++i) {
            if (r>0) {
                end++;
                r--;
            }
            cout << start << " "<< end << endl;
            MPI_Send(&a[start], end-start, MPI_INT, i, 0 , MPI_COMM_WORLD);
            MPI_Send(&b[start], end-start, MPI_INT, i, 0 , MPI_COMM_WORLD);

            start = end;
            end += dim;
        }
        start = 0;
        int count;
        for (int i = 1; i < size; ++i) {
            MPI_Recv(c + start, dim + 1, MPI_INT, i, 1 , MPI_COMM_WORLD, &status);
            MPI_Get_count(&status, MPI_INT, &count);

            start += count;
        }
        auto endTime = MPI_Wtime();
        print(c,N);

        cout << "Time: " << endTime - startTime << " sec" << endl;
    }
    else {
        int count;

        MPI_Recv(a,dim+1, MPI_INT, 0, 0 , MPI_COMM_WORLD, &status);
        MPI_Recv(b,dim+1, MPI_INT, 0, 0 , MPI_COMM_WORLD, &status);
        MPI_Get_count(&status, MPI_INT, &count);


        for (int i=0; i< count; ++i) {
            c[i] = a[i] + b[i];

        }

        MPI_Send(c, count, MPI_INT, 0 , 1 , MPI_COMM_WORLD);

    }

    MPI_Finalize();
    return 0;
}