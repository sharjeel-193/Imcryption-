from PIL import Image
import numpy as np



def encode_str(str_input):
    output = []
    length=len(str_input)
    for x in range(length):
      if str_input[x] == ' ':
        resLet = ord(str_input[x])
        output.append(resLet)
      elif str_input[x] == '.':
        resLet = ord(str_input[x])
        output.append(resLet)
      elif str_input[x] == ',':
        resLet = ord(str_input[x])
        output.append(resLet)
      else:
        size = (length-x)%26
        resLet = ord(str_input[x])+size
        if resLet > 122:
            temp = resLet - 123
            resLet = 97+temp
        output.append(resLet)
    return output


def hash_enc_str(enc_str):
    for x in range(len(enc_str)):
      if enc_str[x] == 32:
        enc_str[x] = 31
      elif enc_str[x] == 46:
        enc_str[x] = 30
      elif enc_str[x] == 44:
        enc_str[x] = 29
      else:
        enc_str[x] = enc_str[x] % 96
    return enc_str

def encrypt_msg(input):
    small_ltr = input.lower()
    input_arr = list(small_ltr)
    print({'Small Letter Array': input_arr})
    enc_str = encode_str(input_arr)
    print({'Encoded String': enc_str})
    final_out = hash_enc_str(enc_str)
    print({'Hashed String': final_out})
    return final_out


def decimalToBinary(n):
    return bin(n).replace("0b", "")

def modifyBit( n,  p,  b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)

def imageManipulation(img, input, key):

    # img = cv2.imread("lena.png")
    # blue, green, red = cv2.split(img)
    photo= Image.open(img).convert('RGB')
    newImgArr = np.asarray(photo).copy()
    img_shape = newImgArr.shape
    print({'Shape': img_shape})

    flat_img = newImgArr.reshape(newImgArr.shape[0]*newImgArr.shape[1], newImgArr.shape[2] )
    flat_img = lock(key,flat_img)

    # print(newImgArr)
    count = 0
    for i in range(0, len(flat_img)-1, 2):
        letter_binary = decimalToBinary(input[count])
        if len(letter_binary) == 1:
            temp = '0000'
            letter_binary = temp + letter_binary
        elif len(letter_binary) == 2:
            temp = '000'
            letter_binary = temp + letter_binary
        elif len(letter_binary) == 3:
            temp = '00'
            letter_binary = temp + letter_binary
        elif len(letter_binary) == 4:
            temp = '0'
            letter_binary = temp + letter_binary

        # print(letter_binary)
        # print("\n")

        flat_img[i][0] = modifyBit(flat_img[i][0], 0, int(letter_binary[0],10))
        flat_img[i][1] = modifyBit(flat_img[i][1], 0, int(letter_binary[1],10))
        flat_img[i+1][0] = modifyBit(flat_img[i+1][0], 0, int(letter_binary[2],10))
        flat_img[i+1][1] = modifyBit(flat_img[i+1][1], 0, int(letter_binary[3],10))
        flat_img[i+1][2] = modifyBit(flat_img[i+1][2], 0, int(letter_binary[4],10))
        count = count + 1


        if len(input) == count:
            flat_img[i+2][0] = modifyBit(flat_img[i+1][0], 0, 0)
            flat_img[i+2][1] = modifyBit(flat_img[i+1][1], 0, 0)
            flat_img[i+3][0] = modifyBit(flat_img[i+2][0], 0, 0)
            flat_img[i+3][1] = modifyBit(flat_img[i+2][1], 0, 0)
            flat_img[i+3][2] = modifyBit(flat_img[i+2][2], 0, 0)
            break;
    newImgArr = flat_img.reshape(img_shape)
    return Image.fromarray(newImgArr)


def encodeMsgintoImg(img, msg, key):
    print({'Size of Message': len(msg)})
    encMsg = encrypt_msg(msg)
    encImg = imageManipulation(img, encMsg, key)
    # encImg.save('enc_img.png')
    return encImg


def decimalToBinary(n):
    return bin(n).replace("0b", "")

def hash_dec(input):
    for x in range(len(input)):
      if input[x] == 31:
        input[x] = 32
      elif input[x] == 30:
        input[x] = 46
      elif input[x] == 29:
        input[x] = 44
      else:
        input[x] = input[x] + 96
    print({'Hasheed': input})
    return input

def decodeString(string_input):
    decode=[]
    outLength=len(string_input)
    for i in range(outLength):
      if string_input[i] == 32:
        resLet = string_input[i]
        decode.append(chr(resLet))
      elif string_input[i] == 46:
        resLet = string_input[i]
        decode.append(chr(resLet))
      elif string_input[i] == 44:
        resLet = string_input[i]
        decode.append(chr(resLet))
      else:
        size = (outLength-i)%26
        resLet = (string_input[i])-(size)
        if resLet < 97:
            temp = 97 - resLet
            resLet = 123 - temp
        decode.append(chr(resLet))
    print({'Decoded': decode})
    return decode

def decrypt_msg(encMsg):
    dehashed_msg = hash_dec(encMsg)
    decode_msg = decodeString(dehashed_msg)
    return decode_msg


def extractingMessage(img):

    photo= Image.open(img)
    newImgArr = np.asarray(photo).copy()
    img_shape = newImgArr.shape
    print({'Shape': img_shape})

    flat_img = newImgArr.reshape(newImgArr.shape[0]*newImgArr.shape[1], newImgArr.shape[2])

    output = []

    for i in range(0, len(flat_img)-1, 2):
        temp = decimalToBinary(flat_img[i][0])
        number = temp[len(temp)-1]
        temp = decimalToBinary(flat_img[i][1])
        number = number + temp[len(temp)-1]
        temp = decimalToBinary(flat_img[i+1][0])
        number = number + temp[len(temp)-1]
        temp = decimalToBinary(flat_img[i+1][1])
        number = number + temp[len(temp)-1]
        temp = decimalToBinary(flat_img[i+1][2])
        number = number + temp[len(temp)-1]

        value = int(number,2)
        # print(value)

        if value == 0:
            break;
        output.append(value)

    print({'Image Data': output})
    return output

def decodeMsgFromImg(img):
    
    encMsg = extractingMessage(img)
    decMsg = decrypt_msg(encMsg)
    output = ""
    return output.join(decMsg)
    # print({'Output': output.join(decMsg)})


# decodeMsgFromImg('enc_img.png')

def get_lock(img):
  photo= Image.open(img)
  newImgArr = np.asarray(photo).copy()
  img_shape = newImgArr.shape
  print({'Shape': img_shape})

  flat_img = newImgArr.reshape(newImgArr.shape[0]*newImgArr.shape[1], newImgArr.shape[2])
  key = []

  for i in range(len(flat_img)-8, len(flat_img)-1, 2):
    temp = decimalToBinary(int(flat_img[i][0]))
    number = temp[len(temp)-1]
    temp = decimalToBinary(int(flat_img[i][1]))
    number = number + temp[len(temp)-1]
    temp = decimalToBinary(int(flat_img[i+1][0]))
    number = number + temp[len(temp)-1]
    temp = decimalToBinary(int(flat_img[i+1][1]))
    number = number + temp[len(temp)-1]
    temp = decimalToBinary(int(flat_img[i+1][2]))
    number = number + temp[len(temp)-1]

    value = int(number,2)
    # print(value)

    key.append(value)
  print(key)
      
  return key

def lock(pin,flat_img):
  count = 0
  for i in range(len(flat_img)-8, len(flat_img)-1, 2):
      letter_binary = decimalToBinary(int(pin[count]))
      if len(letter_binary) == 1:
          temp = '0000'
          letter_binary = temp + letter_binary
      elif len(letter_binary) == 2:
          temp = '000'
          letter_binary = temp + letter_binary
      elif len(letter_binary) == 3:
          temp = '00'
          letter_binary = temp + letter_binary
      elif len(letter_binary) == 4:
          temp = '0'
          letter_binary = temp + letter_binary

      flat_img[i][0] = modifyBit(flat_img[i][0], 0, int(letter_binary[0],10))
      flat_img[i][1] = modifyBit(flat_img[i][1], 0, int(letter_binary[1],10))
      flat_img[i+1][0] = modifyBit(flat_img[i+1][0], 0, int(letter_binary[2],10))
      flat_img[i+1][1] = modifyBit(flat_img[i+1][1], 0, int(letter_binary[3],10))
      flat_img[i+1][2] = modifyBit(flat_img[i+1][2], 0, int(letter_binary[4],10))
      count = count + 1

  return flat_img






