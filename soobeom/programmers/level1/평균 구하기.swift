//
//  평균 구하기.swift
//  평균 구하기
//
//  Created by 정수범 on 2022/01/27.
//

import Foundation

func solution(_ arr:[Int]) -> Double {
    return Double(arr.reduce(0, +)) / Double(arr.count)
}
