//
//  없는 숫자 더하기.swift
//  없는 숫자 더하기
//
//  Created by 정수범 on 2022/01/26.
//

import Foundation

func solution(_ numbers:[Int]) -> Int {
    return 45 - numbers.reduce(0, +)
}
