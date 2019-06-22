"""
Q-Fighter 
Date:   2019/6/7 
Author: Vitor 
Desc: 
        load and store Q-Table Data 
"""
import numpy as np

class QTableIO(object):
    def q_table_save(self, qTable, output_name):
        out_name = output_name + '.txt'
        print("Output file name is: "+ out_name)
        qTable_slice = qTable.shape[0]
        slice_count = 0
        with open(out_name, 'w') as output_file:
            # output_file.write('# Q-table shape: ' + str(qTable.shape) + '\n')
            output_file.write('# Q-table shape: {0}\n'.format(qTable.shape))
            for data_slice in qTable:
                slice_count += 1
                np.savetxt(output_file, data_slice, fmt='%-7.4f')
                if slice_count < qTable_slice:
                    output_file.write('# Next slice:\n')


    def q_table_load(self, input_name, shape):
        input_data = np.loadtxt(input_name + '.txt')
        print(input_data.shape)
        loaded_data = input_data.reshape(shape)

        return loaded_data


if __name__ == "__main__":
    data_name = 'qtable_data'
    data = np.arange(75).reshape((5,3,5))
    # save test data:
    qt = QTableIO()
    qt.q_table_save(data, data_name)
    # load test data:
    loaded = qt.q_table_load(data_name, data.shape)
    print(loaded)
