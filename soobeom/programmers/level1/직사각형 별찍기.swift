//
//  main.swift
//  직사각형 별찍기
//
//  Created by 정수범 on 2022/01/24.
//

import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])

for _ in 0..<b {
    print(String(repeating: "*", count: a))
}
