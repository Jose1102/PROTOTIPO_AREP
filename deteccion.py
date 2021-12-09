import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket="arepproyecto",Key="autos.jpeg")
    file_content = fileObj["Body"].read()
    response = client.detect_labels(Image = {"S3Object":{"Bucket":"arepproyecto","Name":"autos.jpeg"}},MinConfidence=70)
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])

    return{'statusCode':200,
        'body':json.dumps('hello from lambda')
    }
