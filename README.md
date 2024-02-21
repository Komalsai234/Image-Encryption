
# Image Encryption

## Overview

This project implements Image Encryption and Decryption service that integrates the
Advanced Encryption Standard (AES) with the user option to choose between RSA
(Rivest–Shamir–Adleman) and ECC (Elliptic-Curve Cryptography) for the encryption of
the master key. The service is capable of handling both color and grayscale images,
providing a secure, efficient approach to image encryption.

## Key Features
- **Dual Encryption Mechanism:** Primary encryption with AES and an additional layer of security where the user can choose between RSA or ECC for encrypting the AESmaster key.

- **Unique Identifier for Sessions:** Each encryption process generates a unique UUID, ensuring a secure and private decryption process.

- **Flexible File Formats:** Supports common image formats like JPG, PNG, and JPEG.

- **Highly Secure:** Incorporates RSA and ECC, two of the most secure public-key cryptographic algorithms, along with AES.

## Tech Stack
- Python
- OpenCV
- AWS EC2
- Fast API
- Unicorn
- Duck DNS 

## Installation and Setup

### Setting up Conda Environment
- Create a new Conda environment
```
conda create --name image_encryption python=3.9
```
- Activate the environment
```
conda activate image_encryption
```

### Install the required packages
```
pip install -r requirements.txt
```

## Run the application
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
**⚠ This is process of running the app in the local system. The link to access the user
interface is given below but it is 
available only when the app server is running on AWS EC2 instance.**

### Usage
- Access the application through a web browser at **https://kkvs.duckdns.org/**.

- Follow the on-screen instructions to encrypt and decrypt images. 

- Users can choose between RSA and ECC for the encryption of the AES master key.

## User-Interface (UI)
##
  ![App Screenshot](https://github.com/Komalsai234/Image-Encryption/blob/main/images/fast-api.png)

  ### **Image Encryption**
  - User can choose between ECC & RSA for Public Key Encryption
  ###
  ![App Screenshot](https://github.com/Komalsai234/Image-Encryption/blob/main/images/user-encryption.png)

  ### **Image Decryption**
  - By entering the uuid the user can start decryprtion of the image
  ### 
  ![App Screenshot](https://github.com/Komalsai234/Image-Encryption/blob/main/images/user-decryption.png)

  - User can Download the image by clicking on "Download File" as shown below
  ###
  ![App Screenshot](https://github.com/Komalsai234/Image-Encryption/blob/main/images/decryption-image-download.png)

### 
### Security and Limitations
- Utilizes AES for image encryption, enhanced with RSA or ECC for master key security.

- The UUID must be kept secure for decryption.

- Download limits are set to prevent abuse, with a maximum of 5 downloads per encrypted file.

- Large images may take longer to process

## Instructor 

### Dr. Sunil Kumar S, Assistant Professor, Amrita School of AI


## Contributors

- [P.S.S.Sai Keerthana](https://github.com/saikeerthana234)
- [P. Komal Sai Anurag](https://www.github.com/komalsai234)
- [Udayagiri Varun](https://github.com/VarunUdayagiri)
- [Sejal Singh](https://github.com/sejal923)
