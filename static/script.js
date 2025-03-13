document.addEventListener('DOMContentLoaded', () => {
    const slots = document.querySelectorAll('.slot');
    const spinButton = document.getElementById('spin-button');
    const balanceDisplay = document.getElementById('balance');
    const winAmountDisplay = document.getElementById('win-amount');
    const currentBetDisplay = document.getElementById('current-bet');
    const decreaseBetButton = document.getElementById('decrease-bet');
    const increaseBetButton = document.getElementById('increase-bet');

    let balance = 1000;
    let currentBet = 10;
    let isSpinning = false;

    const symbols = {
        lion: '🦁',
        elephant: '🐘',
        rhino: '🦏',
        protea: '🌺',
        springbok: '🦌',
        diamond: '💎',
        drum: '🥁',
        mask: '🎭'
    };

    // Update displays
    const updateDisplays = () => {
        balanceDisplay.textContent = balance;
        currentBetDisplay.textContent = currentBet;
    };

    // Bet controls
    decreaseBetButton.addEventListener('click', () => {
        if (currentBet > 10) {
            currentBet -= 10;
            updateDisplays();
        }
    });

    increaseBetButton.addEventListener('click', () => {
        if (currentBet < 100 && currentBet + 10 <= balance) {
            currentBet += 10;
            updateDisplays();
        }
    });

    // Spinning animation
    const animateSpinning = () => {
        slots.forEach(slot => {
            slot.classList.add('spinning');
            slot.textContent = symbols[Object.keys(symbols)[Math.floor(Math.random() * 8)]];
        });
    };

    // Stop spinning animation
    const stopSpinning = () => {
        slots.forEach(slot => slot.classList.remove('spinning'));
    };

    // Spin function
    const spin = async () => {
        if (isSpinning || balance < currentBet) return;

        isSpinning = true;
        balance -= currentBet;
        updateDisplays();
        spinButton.disabled = true;

        // Start spinning animation
        const spinInterval = setInterval(animateSpinning, 100);

        try {
            const response = await fetch('/spin');
            const data = await response.json();

            // Continue spinning for at least 2 seconds for effect
            await new Promise(resolve => setTimeout(resolve, 2000));

            clearInterval(spinInterval);
            stopSpinning();

            // Display results
            data.symbols.forEach((symbol, index) => {
                slots[index].textContent = symbols[symbol.name];
            });

            // Update balance and winnings
            balance += data.winnings;
            winAmountDisplay.textContent = data.winnings;
            updateDisplays();

            // Celebrate if won
            if (data.winnings > 0) {
                celebrateWin(data.winnings);
            }
        } catch (error) {
            console.error('Error:', error);
            clearInterval(spinInterval);
            stopSpinning();
        }

        isSpinning = false;
        spinButton.disabled = false;
    };

    // Celebration animation
    const celebrateWin = (amount) => {
        const celebration = document.createElement('div');
        celebration.className = 'celebration';
        celebration.textContent = `+ R${amount}!`;
        document.querySelector('.slot-machine').appendChild(celebration);

        setTimeout(() => celebration.remove(), 2000);
    };

    // Add click event to spin button
    spinButton.addEventListener('click', spin);

    // Initialize displays
    updateDisplays();
});