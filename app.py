from statemachine import StateMachine
from fileparser import FileParser

input_file = 'SampleStateTransitions.csv'
output_file = 'output/StateMachine'
output_format = 'svg'

# Parse csv file
nodes, transitions = FileParser.parse(input_file)

# Create state machine and render it
state_machine = StateMachine(output_format)
state_machine.add(nodes, transitions)
state_machine.render(output_file)