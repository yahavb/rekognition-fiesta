#!/usr/bin/python

import boto3


def detect_text(photo, bucket):
  client=boto3.client('rekognition')
  try:
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
    return len(textDetections)
  except ThrottlingException as te:
    print('ThrottlingException {}'.format(te))
  except ProvisionedThroughputExceededException as pte:
    print('ProvisionedThroughputExceededException {}'.format(pte))
  except Exception as e:
    print('general exception {}'.format(e))
    
def main():
    bucket='yahavb'
    photo='idsample.png'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))

if __name__ == "__main__":
    main()
