from enum import Enum
import boto3
import HTPredBenchCreator


class CELL(Enum):
    TSMC = 'tsmc_cells/'
    SYNOPSIS = 'synopsis_cells/'


def run(event, context):
    s3 = boto3.client('s3')
    file_name = "/tmp/afile"
    s3.download_file('htpred-bucket', event['s3key'], file_name)

    cell = CELL.TSMC.value if event['cell'] == 'tsmc' else CELL.SYNOPSIS.value

    outpf = '/tmp/file'

    if event['function'] == 'benchcreator':
        r = HTPredBenchCreator.Creator(file_name, cell, event['main_module'])
        s = open(outpf, 'w')
        s.write(r.convert())
        s.close()

    if event['function'] == 'featureextractor':
        r = HTPredBenchCreator.FeatureExtractor(file_name, cell, event['main_module'])
        r.getfeatures(outpf, ['preferences/mux_list.txt'])

    s3.upload_file(outpf, 'htpred-bucket', event['s3outputkey'])

    return {"STATUS":"SUCCESS"}