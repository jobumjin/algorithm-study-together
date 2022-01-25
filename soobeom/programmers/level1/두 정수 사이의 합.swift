//
//  main.swift
//  두 정수 사이의 합
//
//  Created by 정수범 on 2022/01/25.
//

import Foundation

func solution(_ a:Int, _ b:Int) -> Int64 {
    var sum = 0
    
    for i in (a>b ? b...a : a...b) {
        sum += i
    }
    return Int64(sum)
}
