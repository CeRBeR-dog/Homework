"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. 
Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import re
from datetime import date, timedelta
import secrets
import string
from typing import Optional, Tuple


class User:
    
	def __init__(self, 
			  name: str, 
			  login: str, 
			  password: Optional[str] = None, 
			  is_blocked: bool = False, 
			  subscription_date: Optional[date] = None, 
			  subscription_mode: str = "free"):
		
		self.name = name
		self.login = login

		if password is None:
			password = self._generate_password()
			print("Сгенерирован пароль: ", password)

		self.password = password

		self.is_blocked = bool(is_blocked)

		if subscription_date is None:
			subscription_date = date.today() + timedelta(days=30)
			subscription_mode = 'free'

		self.subscription_date = subscription_date
		self.subscription_mode = subscription_mode
	

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		pattern_name = r'^[А-Яа-яЁё]+$' 
		if not re.fullmatch(pattern_name, value):
			raise ValueError('Имя может содержит только буквы русского алфавита')

		self._name = value


	@property
	def login(self):
		return self._login
		
	@login.setter
	def login(self, value):
		patter_login = r'^[A-Za-z0-9_]$'
		if not re.fullmatch(patter_login, value) or len(value)>6:
			raise ValueError('Логин может содержать только латинские ' \
			'буквы цифры и черту подчеркивания быть не менее 6 символов')

		self._login = value
	

	@property
	def password(self):
		return self._password
	
	@password.setter
	def password(self, value):
		patter_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)$'
		if not re.fullmatch(patter_password, value):
			raise ValueError(' пароль - может содержать  только латинские буквы цифры. Обязательные условия:' \
				'\nсодержит менее шести символов'\
                '\nсодержит строчную букву'\
                '\nсодержит заглавную букву'\
                '\nсодержит число')

		self._password = value
	
	def _generate_password(self) -> str:
		length = 6
		
		char = [
			secrets.choice(string.ascii_lowercase),
			secrets.choice(string.ascii_uppercase),
			secrets.choice(string.digits),
			]
		char += [	
			secrets.choice(string.ascii_letters + string.ascii_uppercase + string.digits)
			for _ in range(length-1)
		]
		secrets.SystemRandom.shuffle(char)
		return ''.join(char)

	
	@property
	def subscription_date(self) -> date:
		return self._subscription_date
	
	@subscription_date.setter
	def subscription_date(self, value: date):
		if not isinstance(value, date):
			raise ValueError('subscription_date должен быть datetime.date')

		self._subscription_date = value
		self.subscription_mode = "paid"


	@property
	def subscription_mode(self) -> str:
		return self._subscription_mode
	
	@subscription_mode.setter
	def subscription_mode(self, value: str):
		if value not in ('free','paid'):
			return ('subscription_mode должен иметь значение "free" или "paid"')
		
		self._subscription_mode = value

	# Методы
	def bloc(self, flag: bool):
		self.is_blocked = bool(flag)

	def check_subscr(self, on_date: Optional[date] = None) -> Tuple[bool, str, int]:
		"""Возвращает (действует ли, вид подписки, сколько дней осталось)"""
		if not isinstance(on_date, date):
			raise ValueError('on_date должен быть datetime.time или None')
		
		if on_date is None:
			on_date = date.today()
		
		days_left = (self.subscription_date - on_date).days
		active = days_left >= 0
		return active, self.subscription_mode, max(days_left,0)
	
	def change_pass(self, new_pass: Optional[str] = None) -> str:
		"""Если new_pass None — генерируем, иначе валидируем и присваиваем. Возвращаем новый пароль."""
		if new_pass is None:
			new_pass = self._generate_password
			print("Сгенерирован пароль: ", new_pass)
		
		self.password = new_pass
		return new_pass
	
	def get_info(self) -> str:
		if self.is_blocked:
			return "Пользователь заблокирован"
		
		info = (
			f"Имя: {self.name}\n"
			f"Логин: {self.login}\n" 
			f"Подписка до: {self._subscription_date} ({self._subscription_mode})\n" 
		)
		return info
		 
	
	
		
