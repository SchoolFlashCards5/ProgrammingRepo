let bal = 100;
let winorlose = "";
document.getElementById("balance").textContent = bal; //prints out balance before anything so user knows what they start with

function resetbal() {
  bal = 100 //resets balance to 0
  winorlose = "balance reset"; //resets win or lose text to balance reset to assure user it was reset to 100
  document.getElementById("balance").textContent = bal; //printsout balance so the user has visual proof of reset
  console.log("balance reset to 100")
}

function placeBet() {
  let betAmount = Number(document.getElementById("betInput").value);
  if (betAmount <= 0 || betAmount > bal) {
    alert("Invalid bet; you cant bet more than you have or 0 or a negative OR more than you have")
    return;
  }

  const button = document.getElementById("incrementButton");
  button.disabled = true;

  const display = document.getElementById("winorlose");

  let frames = [".", "..", "..."];
  let frameIndex = 0;

  const animInterval = setInterval(() => {
    display.textContent = frames[frameIndex];
    frameIndex = (frameIndex + 1) % frames.length;
  }, 150);

  // Total animation = 0.5s for initial frames + 150ms pause on last "..."
  setTimeout(() => {
    clearInterval(animInterval);

    setTimeout(() => { // small delay to show "..." before result
      if (Math.random() < 0.5) {
        bal += betAmount; //win does plus bet amm
        winorlose = "you won"; //sets win or lose display text to win
        console.log("Balance is now " + bal)
      } else {
        bal -= betAmount; //lose does minus bet amm
        winorlose = "sorry you lost :("; //sets win or lose display text to win
        console.log("Balance is now " + bal)
      }

      document.getElementById("balance").textContent = bal;
      display.textContent = winorlose;
      button.disabled = false;
    }, 150); // extra 150ms pause on last "..."
  }, 500);
}
