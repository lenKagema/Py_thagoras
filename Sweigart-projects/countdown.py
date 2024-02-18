import sys
import time
import sevseg

seconds_left = 30

try:
    # Main program loop
    while True:
        # Clear the screen by printing several newlines:
        print('\n' * 5)

        hours = str(seconds_left // 3600)
        minutes = str((seconds_left % 3600) // 60)
        seconds = str(seconds_left % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow + '     ' + hMiddleRow + '     ' + hBottomRow)
        print(mTopRow + '  *  ' + mMiddleRow + '  *  ' + mBottomRow)
        print(sTopRow + '  *  ' + sMiddleRow + '  *  ' + sBottomRow)

        if seconds_left == 0:
            print()
            print('     * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        seconds_left -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.
