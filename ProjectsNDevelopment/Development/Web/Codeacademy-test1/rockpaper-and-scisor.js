const getUserChoice = userInput => {
  userInput=userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissor' || userInput === 'bomb') {
    if (userInput === 'bomb'){
      return 'Error 404!'
    }else {
      return userInput;
    }
  } else {
    console.log('Error!');
  }
}

const getComputerChoice= () => {
  let value=Math.floor(Math.random()*3);
  switch(value){
    case 0:
      return 'rock';
    case 1:
      return 'paper';
    default:
      return 'scissor'
  }
}

const determineWinner = (userChoice, computerChoice) => {
  if(userChoice===computerChoice){
    return 'Tie';
  } else {
    if (userChoice ==='rock'){
      if (computerChoice === 'paper'){
        return 'user won!';
      } else {
        return 'computer won!';
      }
    } else if(userChoice === 'paper'){
      if (computerChoice === 'scissor'){
        return 'computer won!';
      } else {
        return 'user won!'
      }
    } else if (userChoice === 'scissor'){
      if (computerChoice === 'rock'){
        return 'computer won!';
      } else {
        return 'user won!';
      } 
    } else if (userChoice === 'bomb'){
      return 'user won!';
    }
  }
} 

let compvalue = getComputerChoice();
let uservalue = getUserChoice('bomb');
let compvalue1 = getComputerChoice();
console.log(determineWinner(uservalue, compvalue),uservalue,compvalue);
console.log("PC against itself! (user is compvalue1)", determineWinner(compvalue,compvalue1),compvalue1,compvalue)