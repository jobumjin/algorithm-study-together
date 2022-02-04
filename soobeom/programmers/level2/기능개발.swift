//
//  main.swift
//  기능개발
//
//  Created by 정수범 on 2022/02/04.
//

import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
  var prog = progresses
  var speed = speeds
  var answer: [Int] = []
  
  repeat {
    var count = 0
    
    // progresses를 speeds만큼 더해준다
    for idx in 0..<prog.count {
      prog[idx] += speed[idx]
    }

    repeat {
      // 2) prog의 첫번째 값이 100이상인지 체크해준다
      if prog[0] >= 100 {
        // 100이상이 경우, prog의 값과 speed의 값을 지워주고, count를 세어준다
        prog.removeFirst()
        speed.removeFirst()
        count += 1
      } else {
        break
      }
      // prog의 첫번째 값이 100이상이 아닐 때까지 반복해준다
      // 100이상이 아닐 경우 break로 repeat-while문을 탈출하게 된다
    } while !prog.isEmpty
    
    // 3) count가 0이상인 경우(배포한 경우), answer에 해당 값을 담아준다
    if count > 0 {
      answer.append(count)
    }
    // prog에 값이 없을 때 까지 위 모든 과정을 반복한다
  } while !prog.isEmpty
    
  return answer
}

