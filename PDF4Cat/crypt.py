import os

from .cat import PDF4Cat

class Crypter(PDF4Cat):
	def __init__(self, *args):
		super(Crypter, self).__init__(*args)

	# @PDF4Cat.run_in_subprocess
	def crypt_to(self, user_passwd: str = None, 
		owner_passwd: str = None, 
		perm: dict = None, 
		R: int = 4, 
		output_pdf: str = None) -> None:

		if not output_pdf:
			output_pdf = os.path.join(self.pdf_path, self.pdf_name)

		if not perm:
			perm = {'extract': False,}

		if not user_passwd:
			user_passwd = owner_passwd
		elif not user_passwd:
			owner_passwd = user_passwd
		elif not user_passwd and not owner_passwd:
			raise TypeError("Missing user or owner password!")


		self.pdf.save(output_pdf, encryption=self.pdfEncryption(
			user=user_passwd, owner=owner_passwd, R=R,
			allow=self.pdfPermissions(**perm)
			))

	def decrypt(self, passwd: str, output_pdf: str = None) -> None:
		pass


