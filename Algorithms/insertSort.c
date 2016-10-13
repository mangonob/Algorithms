//
//  insertSort.c
//  Algorithms
//
//  Created by Trinity on 16/10/12.
//  Copyright © 2016年 Trinity. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include "common.h"


void insertSortMain() {
    void insertSort(int *, int);
    printf("please input some integer to sort (end with -1): \n");
    
    int a[MAX_ELEMENT_NUM], i;
    
    for (i = 0; scanf("%d", a + i), a[i] != -1; ++i);
    insertSort(a, i);
    
    for (int idx = 0; idx < i; ++idx) printf("%d ", a[idx]);
    printf("\n");
}

void insertSort(int *arr, int n) {
    for (int i = 1; i < n; ++i) {
        int t = arr[i];
        int j;
        for (j = i - 1; j >= 0 && arr[j] > t; --j) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = t;
    }
}