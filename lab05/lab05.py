from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import random
from util.llm_utils import run_console_chat, tool_tracker

# beauty of Python
@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def roll_for(skill, dc, player):
    n_dice = 1
    sides = 20
    roll = sum([random.randint(1, sides) for _ in range(n_dice)])
    if roll >= int(dc):
        return f'{player} rolled {roll} for {skill} and succeeded!'
    else:
        return f'{player} rolled {roll} for {skill} and failed!'

def process_response(self, response):
    # Fill out this function to process the response from the LLM
    # and make the function call 

    if response.message.tool_calls:
        #extract the tool call information
        tool_call = response.message.tool_calls[0]
        function_name = tool_call.function.name
        arguments = tool_call.function.arguments
        
        #process the function call and get the result
        result = process_function_call(tool_call.function)
        
        #append the result as a response to the tool call
        response.message.tool_calls[0].content = result
    
    return response

run_console_chat(template_file='lab05/lab05_dice_template.json',
                 process_response=process_response)
