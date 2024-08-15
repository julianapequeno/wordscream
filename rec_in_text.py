from psychopy import visual, core, event
 
## WORKING FOR JUST ONE LINE
def get_word_positions(text_stim):
    """
    Approximate the positions of words in a TextStim.
    """
    words = text_stim.text.split()
    word_positions = []
    
    # Create a TextStim for each word to get its width
    current_x = text_stim.pos[0] - (text_stim.boundingBox[0] / 2)  # Start at the left edge of the text area

    for word in words:
        # Create a temporary TextStim to measure the word width
        word_stim = visual.TextStim(win, text=word, pos=(current_x, text_stim.pos[1]), color=text_stim.color, units='pix')
        word_width, word_height = word_stim.boundingBox
        
        # Calculate the position (center of the word)
        word_position = (current_x + word_width / 2, text_stim.pos[1])
        
        # Store word info
        word_positions.append((word, word_position, word_width, word_height))
        
        # Move to the next position (accounting for space between words)
        current_x += word_width + 5 # Assuming a space width of text height for simplicity
    
    return word_positions

# Create a window
win = visual.Window([1200, 1000], color='white', units='pix')

# Define the text
text_content = 'Hello World Example Textthisith JUliana is beautiful'
text_stim = visual.TextStim(win, text=text_content, pos=(0, 0), color='black', units='pix')

# Draw the text to calculate the positions
text_stim.draw()

# Calculate positions of each word
word_positions = get_word_positions(text_stim)

# Draw rectangles around each word
for word, pos, width, height in word_positions:
    rect_stim = visual.Rect(win, width=width * 1.1, height=height * 1.1,  # Some padding
                            pos=pos, lineColor='black', fillColor='lightgrey', units='pix')
    rect_stim.draw()

# Draw the text again so it appears on top of the rectangles
text_stim.draw()

# Display everything
win.flip()

# Wait for a key press to close the window
event.waitKeys()
win.close()
core.quit()
