import csv


class FileParser(object):

    @staticmethod
    def parse(input_file):
        """Reads the states and transitions from a file."""

        nodes = set()
        transitions = {}

        with open(input_file, newline='') as csv_file:
            state_reader = csv.reader(csv_file, delimiter=',', quotechar='|')

            header_row = []
            for row in state_reader:

                if len(header_row) == 0:
                    header_row = row
                else:
                    state_name = row[0]

                    nodes.add(state_name)

                    # Get transitions
                    for idx, new_state in enumerate(row[1:len(header_row)]):

                        if new_state != '' and new_state != state_name:
                            key = (state_name, new_state)

                            if key in transitions:
                                transitions[key] = '{0}\n{1}'.format(transitions[key], header_row[idx + 1])
                            else:
                                transitions[key] = header_row[idx + 1]
        return nodes, transitions
