from google.cloud import storage
import os


def upload_file_to_bucket(bucket_name, source_file_name, destination_blob_name):
    # Create a client for Google Cloud Storage
    client = storage.Client()

    # Get the bucket the file will be uploaded to
    bucket = client.bucket(bucket_name)

    # Create the object used to upload the file (blob) in this bucket
    blob = bucket.blob(destination_blob_name)
    # Upload the file to the bucket
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded as {destination_blob_name} to bucket {bucket_name}.")
