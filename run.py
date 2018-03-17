from umbral import keys, pre

# alices_private_key = keys.UmbralPrivateKey.gen_key()
# alices_public_key = alices_private_key.get_pubkey()

# print (type(alices_private_key))
# print (type(alices_public_key))

# print(type(alices_public_key)==keys.UmbralPublicKey)


# plaintext = b'Proxy Re-encryption is cool!'

# ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)

# cleartext = pre.decrypt(capsule, alices_private_key,
#                            ciphertext, alices_public_key)

# print(cleartext)


# bobs_private_key = keys.UmbralPrivateKey.gen_key()
# bobs_public_key = bobs_private_key.get_pubkey()


# kfrags = pre.split_rekey(alices_private_key, bobs_public_key, 10, 20)

# for kfrag in kfrags:
#     cfrag = pre.reencrypt(kfrag, capsule)
#     capsule.attach_cfrag(cfrag)


# cleartext = pre.decrypt(capsule, bobs_private_key,
#                            ciphertext, alices_public_key)


# print (alices_private_key)
# print (alices_public_key)







def generate_privkey():

	key = keys.UmbralPrivateKey.gen_key()
	return key


def get_pubkeyfrompriv(priv_key_object):

	pubkey = priv_key_object.get_pubkey()
	return pubkey


def encrypt_message(receiver_pub_key, plaintext, sender_priv_key):

	ciphertext, capsule = pre.encrypt(receiver_pub_key, plaintext)

	kfrags = pre.split_rekey(sender_priv_key, receiver_pub_key, 10, 20)

	for k in kfrags:

		cfrag = pre.reencrypt(kfrag, capsule)
		capsule.attach_cfrag(cfrag)



	return ciphertext, capsule


def decrypt_message(capsule, receiver_priv_key, ciphertext, sender_pub_key):

	cleartext = pre.decrypt(capsule, receiver_priv_key,
                           ciphertext, sender_pub_key)

	return cleartext


def get_raw_key(key_object):

	return key_object.to_bytes()

def generate_keyobject_from_raw(raw_key):

	key = keys.UmbralPrivateKey.from_bytes(raw_key)
	return key


def capsule_to_bytes(capsule_object):

	return capsul_object.to_bytes()


def bytes_to_capsule(raw_bytes):

	capsule = pre.capsule.from_bytes(raw_bytes)

	return capsule



