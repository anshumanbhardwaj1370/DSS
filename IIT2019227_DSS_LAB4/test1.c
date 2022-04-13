// include all basic libraries mpi.h being the most important one in our case

// to compile this program we can give command
            // mpicc test1.c -o test1
// to run this program we can give command
            // mpirun -n 4 ./test1 8

#include <mpi.h>  		
#include <stdio.h> 		 
#include <malloc.h>
#include <time.h>

int main(int argc ,char **argv)
{
    int er=MPI_Init(&argc,&argv);
    
    if (er != MPI_SUCCESS){
		printf("\nError initializing MPI.\n");
		MPI_Abort(MPI_COMM_WORLD, er);
    } 

    int node,sz;

    MPI_Comm_rank(MPI_COMM_WORLD, &node);
    MPI_Comm_size(MPI_COMM_WORLD, &sz);

    int n=atoi(argv[1]);
        // siize of array
    int *arr;
    int k=n/sz;
    int sum_array=malloc(sz(sizeof(int)));
    // sumarray includes the sum calcluated by 4 processors
    int *child=malloc(k*sizeof(int));

    if (node==0)
    {
        arr=malloc(n*sizeof(int));
        for (int i=0;i<n;i++)
        {
            arr[i]=rand()%100;
        }
                // randomly generated the array 
        printf("Generated array is \n");
        for (int i=0;i<n;i++)
        {
            printf("%d ",arr[i]);

        }
        printf("\n");
    }

    MPI_Scatter(arr, k ,MPI_INT, child, k, MPI_INT, 0, MPI_COMM_WORLD);
        // here i have divided the main array into sz chuncks
    int partial_sum=0;

    for (int i=0;i<k;i++)
    {
        partial_sum+=child[i];
    }

    MPI_Gather(&partial_sum, 1, MPI_INT, sum_array, 1, MPI_INT, 0, MPI_COMM_WORLD);
    // MPI_Gather
    // here we accumaulated results by 4 processors
    if (node==0)
    {
        int sum=0;
        for (int i=0;i<sz;i++)
        {
            sum+=sum_array[i];
        }

        printf("final sum is %d\n",sum);

    }
    MPI_Finalize();
}