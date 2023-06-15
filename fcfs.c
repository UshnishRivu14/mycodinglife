#include<stdio.h>

void sort_by_arrival_time(int at[], int bt[], int pid[], int n){
int i, j, temp;
for(i=0;i<n;i++){
    for(j=i+1;j<n;j++){
        if(a[i]>a[j]){  
          temp = at[i];
          at[i] = at[j];
          at[j] = temp;
          
          temp = bt[i];
          bt[i] = bt[j];
          bt[j] = temp;
          
          temp = pid[i];
          pid[i] = pid[j];
          pid[j] = temp;
          }   
     }
}
};
int main(){
    int at[50], bt[50], pid[50], ct[50], wt[50], tat[50],i,j ,ttat=0, twt=0;
    int n;
    float avg_tat = 0, avg_wt = 0;
    
    printf("Enter the number of processes: ");
    scanf("%d",&n);
    printf("Enter the number ");
    
    sort_by_arrival_time(at,bt,pid,n);
    ct[0] = at[0] + bt[0];
    for(i=1;i<n;i++){
        ct[i] = ct[i-1] + bt[i];                                  
}
    avg_tat = ttat/n;
    avg_wt = twt/n;
    printf("");
    printf("");
    
    return 0;
}    
