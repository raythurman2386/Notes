# https://www.hackerrank.com/challenges/insertionsort1/problem
def insertion_sort(n, arr):
    i = len(arr) - 1
    val = arr[i]

    while val < arr[i - 1]:
        arr[i] = arr[i - 1]
        print(" ".join(arr))
        i -= 1

    arr[i] = val
    x = " ".join(arr)
    print(x)

insertion_sort(5, ["2", "4", "6", "8", "3"])

"""
JS Implementation

// Complete the insertionSort1 function below.
function insertionSort1(n, arr) {
    let i = arr.length-1;
    let val = arr[i];

    while(val < arr[i-1]){
        arr[i] = arr[i-1];
        console.log(arr.join(` `));
        i--;
    }
    arr[i] = val;
    console.log(arr.join(` `));
}
"""