"""
Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе 
данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или 
создавать пользователя в базе данных с помощью SQL и использовать его при любых изменениях.
Или реализовать все на SQLAlchemy.


* в базе данных создать таблицу предоставляемых услуг со след полями
	название
	тип (1 - платная 0 - бесплатная)
	стоимость 
	период в днях
** в класс пользователя добавить методы:
	добавить услугу (услуг у одного пользователя может быть несколько)
	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
	удалить услугу
*** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
	Меню:
		1 - показать пользователей
		2 - информация о пользователе (в т.ч. и подключенные услуги)
		3 - список услуг		
		4 - показать пользователей с определенной услугой
		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги 
 
	
 
"""


import re
from datetime import date, timedelta
import secrets
import string
from typing import Optional, Tuple
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, query

Base = declarative_base()


class Service(Base):
	__tablename__ = "service"

	id_s = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	type_sub = Column(Integer, nullable=False)
	price = Column(Float, default=0)
	period_days = Column(Integer, nullable=False)

	users = relationship("UserService", back_populates="service")

	def __str__(self):
		t = "Платная" if self.type_sub else "Бесплатная"
		return f"{self.id_s}. {self.name} ({t}, {self.period_days} дн.)"


class UserModel(Base):
	__tablename__="users"

	id_u = Column(Integer, primary_key=True)
	name = Column(String)
	login = Column(String, unique= True)
	password = Column(String)
	is_blocked = Column(Boolean, default=False)

	services = relationship("UserService", back_populates="user")


class UserService(Base):
	__tablename__="user_service"

	id_us = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id_u"))
	service_id = Column(Integer, ForeignKey("service.id_s"))

	start_date = Column(Date)
	end_date = Column(Date)

	user = relationship("UserModel", back_populates="services")
	service = relationship("Service", back_populates="users")


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
		patter_login = r'^[A-Za-z0-9_]{6,}$'
		if not re.fullmatch(patter_login, value) :
			raise ValueError('Логин может содержать только латинские ' \
			'буквы цифры и черту подчеркивания быть не менее 6 символов')

		self._login = value
	

	@property
	def password(self):
		return self._password
	
	@password.setter
	def password(self, value):
		patter_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{6,}$'
		if not re.fullmatch(patter_password, value):
			raise ValueError(' пароль - может содержать  только латинские буквы цифры. Обязательные условия:' \
				'\nсодержит более шести символов'\
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
			for _ in range(length-3)
		]
		secrets.SystemRandom().shuffle(char)
		return ''.join(char)

	
	@property
	def subscription_date(self) -> date:
		return self._subscription_date
	
	@subscription_date.setter
	def subscription_date(self, value: date):
		if not isinstance(value, date):
			raise ValueError('subscription_date должен быть datetime.date')

		self._subscription_date = value
		


	@property
	def subscription_mode(self) -> str:
		return self._subscription_mode
	
	@subscription_mode.setter
	def subscription_mode(self, value: str):
		if value not in ('free','paid'):
			raise ValueError('subscription_mode должен иметь значение "free" или "paid"')
		
		self._subscription_mode = value

	# Методы
	def bloc(self, flag: bool):
		self.is_blocked = bool(flag)

	def extend_subscription(self, days: int):
		if days <= 0:
			raise ValueError('days должен быть положительным')

		self.subscription_date += timedelta(days=days)
		self.subscription_mode = 'paid'

	def check_subscr(self, on_date: Optional[date] = None) -> Tuple[bool, str, int]:
		"""Возвращает (действует ли, вид подписки, сколько дней осталось)"""
		if on_date is None:
			on_date = date.today()
		
		if not isinstance(on_date, date):
			raise ValueError('on_date должен быть datetime.date или None')
		
		
		days_left = (self.subscription_date - on_date).days
		active = days_left >= 0
		return active, self.subscription_mode, max(days_left,0)
	
	def change_pass(self, new_pass: Optional[str] = None) -> str:
		"""Если new_pass None — генерируем, иначе валидируем и присваиваем. Возвращаем новый пароль."""
		if new_pass is None:
			new_pass = self._generate_password()
			print("Сгенерирован пароль: ", new_pass)
		
		self.password = new_pass
		return new_pass
	
	def get_info(self) -> str:
		if self.is_blocked:
			return "Пользователь заблокирован"
		
		info = (
			f"Имя: {self.name}\n"
			f"Логин: {self.login}\n" 
			f"Подписка до: {self.subscription_date} ({self.subscription_mode})\n" 
		)
		return info
		 
	def save(self, session):

		user = session.query(UserModel).filter_by(login=self.login).first()

		if user is None:

			user = UserModel(
				name = self.name,
				login = self.login,
				password = self.password,
				is_blocked =self.is_blocked
			)
			session.add(user)
		
		else:
			user.name = self.name
			user.password = self.password
			user.is_blocked = self.is_blocked
		
		session.commit()
		return user
	
	def add_service(self, session, service: Service):

		user = session.query(UserModel).filter_by(login=self.login).first()

		today = date.today()
		end = today + timedelta(days=service.period_days)

		us = UserService(
			user=user,
			service=service,
			start_date=today,
			end_date=end
		)

		session.add(us)
		session.commit()
	
	def extend_service(self, session, service: Service):

		user = session.query(UserModel).filter_by(login=self.login).first()
		today = date.today()

		us = session.query(UserService).filter_by(
			user_id = user.id_u,
			service_id = service.id_s
		).first()

		if us and us.end_date >= today:
			us.end_date += timedelta(days=service.period_days)

		else:
			self.add_service(session, service)

		session.commit()

	def delete_service(self, session, service: Service):

		user = session.query(UserModel).filter_by(login=self.login).first()

		us = session.query(UserService).filter_by(
			user_id = user.id_u,
			service_id = service.id_s
		).first()

		if us:
			session.delete(us)
			session.commit()
		






if __name__ == "__main__":

	engine = create_engine("sqlite:///app.db")
	Base.metadata.create_all(engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	user = User("Иван", "ivan123", "Qwerty1")
	user.save(session)
	