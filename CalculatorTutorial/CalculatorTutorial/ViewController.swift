//
//  ViewController.swift
//  CalculatorTutorial
//
//  Created by Lakshmi Maduri on 4/2/25.
//

import UIKit

class ViewController: UIViewController {
//  variables for all the fields/ui components on the screen
    @IBOutlet weak var firstNumber: UITextField!
    @IBOutlet weak var secondNumber: UITextField!
    @IBOutlet weak var result: UITextView!
    
    var resultNumber = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func plusClick(_ sender: Any) {
        if let firstText = Int(firstNumber.text!){
            if let secondText = Int(secondNumber.text!){
                resultNumber = firstText + secondText
                result.text = String(resultNumber)
            }
        }
    }
    
    @IBAction func minusClick(_ sender: Any) {
        if let firstText = Int(firstNumber.text!){
            if let secondText = Int(secondNumber.text!){
                resultNumber = firstText - secondText
                result.text = String(resultNumber)
            }
        }
    }
    
    @IBAction func multiplyClick(_ sender: Any) {
        if let firstText = Int(firstNumber.text!){
            if let secondText = Int(secondNumber.text!){
                resultNumber = firstText * secondText
                result.text = String(resultNumber)
            }
        }
    }
    
    @IBAction func divideClick(_ sender: Any) {
        if let firstText = Int(firstNumber.text!){
            if let secondText = Int(secondNumber.text!){
                resultNumber = firstText / secondText
                result.text = String(resultNumber)
            }
        }
    }
    
}

