let result = document.getElementById("result");
let calculation = "";

function appendNumber(number) {
  calculation += number;
  result.value = calculation;
}

function appendOperator(operator) {
  calculation += operator;
  result.value = calculation;
}

function calculate() {
  try {
    result.value = eval(calculation);
  } catch (error) {
    result.value = "Error";
  }
}

function clearResult() {
  calculation = "";
  result.value = "";
}
