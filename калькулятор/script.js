// Функция для нахождения НОД (наибольший общий делитель)
function findGCD(a, b) {
    a = Math.abs(a);
    b = Math.abs(b);
    
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    
    return a;
}

// Функция для сокращения дроби
function reduceFraction(numerator, denominator) {
    if (denominator === 0) {
        throw new Error("Знаменатель не может быть равен нулю!");
    }
    
    // Определяем знак дроби
    let sign = 1;
    if (numerator < 0 && denominator > 0) {
        sign = -1;
        numerator = Math.abs(numerator);
    } else if (numerator > 0 && denominator < 0) {
        sign = -1;
        denominator = Math.abs(denominator);
    } else if (numerator < 0 && denominator < 0) {
        sign = 1;
        numerator = Math.abs(numerator);
        denominator = Math.abs(denominator);
    }
    
    // Находим НОД
    let gcd = findGCD(numerator, denominator);
    
    // Сокращаем дробь
    let reducedNumerator = sign * (numerator / gcd);
    let reducedDenominator = denominator / gcd;
    
    return {
        numerator: reducedNumerator,
        denominator: reducedDenominator
    };
}

// Функция сложения дробей
function addFractions(num1, den1, num2, den2) {
    let newNumerator = num1 * den2 + num2 * den1;
    let newDenominator = den1 * den2;
    return reduceFraction(newNumerator, newDenominator);
}

// Функция вычитания дробей
function subtractFractions(num1, den1, num2, den2) {
    let newNumerator = num1 * den2 - num2 * den1;
    let newDenominator = den1 * den2;
    return reduceFraction(newNumerator, newDenominator);
}

// Функция умножения дробей
function multiplyFractions(num1, den1, num2, den2) {
    let newNumerator = num1 * num2;
    let newDenominator = den1 * den2;
    return reduceFraction(newNumerator, newDenominator);
}

// Функция деления дробей
function divideFractions(num1, den1, num2, den2) {
    if (num2 === 0) {
        throw new Error("Деление на ноль невозможно!");
    }
    let newNumerator = num1 * den2;
    let newDenominator = den1 * num2;
    return reduceFraction(newNumerator, newDenominator);
}

// Основная функция расчета с параметрами
function calculate(operation) {
    try {
        // Получаем значения из полей ввода
        let numerator1 = parseInt(document.getElementById('num1').value);
        let denominator1 = parseInt(document.getElementById('den1').value);
        let numerator2 = parseInt(document.getElementById('num2').value);
        let denominator2 = parseInt(document.getElementById('den2').value);
        
        // Проверяем корректность ввода
        if (isNaN(numerator1) || isNaN(denominator1) || 
            isNaN(numerator2) || isNaN(denominator2)) {
            throw new Error("Пожалуйста, заполните все поля!");
        }
        
        if (denominator1 === 0 || denominator2 === 0) {
            throw new Error("Знаменатель не может быть равен нулю!");
        }
        
        let result;
        let operationSymbol;
        
        // Выполняем операцию в зависимости от параметра
        switch(operation) {
            case 'add':
                result = addFractions(numerator1, denominator1, numerator2, denominator2);
                operationSymbol = '+';
                break;
            case 'subtract':
                result = subtractFractions(numerator1, denominator1, numerator2, denominator2);
                operationSymbol = '-';
                break;
            case 'multiply':
                result = multiplyFractions(numerator1, denominator1, numerator2, denominator2);
                operationSymbol = '×';
                break;
            case 'divide':
                result = divideFractions(numerator1, denominator1, numerator2, denominator2);
                operationSymbol = '÷';
                break;
            default:
                throw new Error("Неизвестная операция!");
        }
        
        // Формируем строку результата
        let resultText = `${numerator1}/${denominator1} ${operationSymbol} ${numerator2}/${denominator2} = ${result.numerator}/${result.denominator}`;
        
        // Если дробь целая
        if (result.denominator === 1) {
            resultText = `${numerator1}/${denominator1} ${operationSymbol} ${numerator2}/${denominator2} = ${result.numerator}`;
        }
        
        // Выводим результат
        document.getElementById('result').textContent = resultText;
        document.getElementById('result').style.color = '#28a745';
        
    } catch (error) {
        document.getElementById('result').textContent = "Ошибка: " + error.message;
        document.getElementById('result').style.color = '#dc3545';
    }
}
// Функция для замены изображения при наведении
function swapImage(buttonElement, newSrc) {
    const img = buttonElement.querySelector('img');
    if (img) {
        img.src = newSrc;
    }
}
