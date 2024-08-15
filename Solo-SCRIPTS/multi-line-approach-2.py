from psychopy import visual, core, event

def get_word_positions(text_stim,height_word):
    """
    Calculate the positions of words in a multi-line TextStim, accounting for varying line lengths.
    """
    lines = text_stim.text.splitlines()
    word_positions = []
    
    # Estimate line height
    line_height = text_stim.height * 1.2
    
    for i, line in enumerate(lines):
        # Create a temporary TextStim to measure the width of the line
        line_stim = visual.TextStim(win, text=line, pos=(0, 0), color=text_stim.color, units='pix',height=height_word)
        line_width, line_height = line_stim.boundingBox
        
        # Determine the starting x position for the current line
        current_x = -line_width / 2
        
        # Calculate y position for the current line
        current_y = text_stim.pos[1] + (len(lines) / 2 - i) * line_height -10
        
        for word in line.split():
            # Create a temporary TextStim to measure the word width
            word_stim = visual.TextStim(win, text=word, pos=(0, 0), color=text_stim.color, units='pix',height=height_word)
            word_width, word_height = word_stim.boundingBox
            
            # Calculate the position (center of the word)
            word_position = (current_x + word_width / 2, current_y)
            
            # Store word info
            word_positions.append((word, word_position, word_width, word_height))
            
            # Move to the next word position (accounting for space between words)
            current_x += word_width + 5 # Space between words (use text size or adjust if needed)
    
    return word_positions

# Create a window
win = visual.Window([800, 600], color='white', units='pix')

# Define the text
text_content = 'Hello World \nJuliana Freire \nPequeno de \nSantiago Carvalho\nShort Text\nAnother Line'
height_word = 50

text_stim = visual.TextStim(win, text=text_content, pos=(0, 0), color='black', units='pix',height=height_word)

# Draw the text to calculate the positions
text_stim.draw()

# Calculate positions of each word
word_positions = get_word_positions(text_stim,height_word)

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
