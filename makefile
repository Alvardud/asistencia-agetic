install:
	pip install requests;
	pip install flask;
	pip install pipdeptree;
	pip install python-dotenv;
	pip install python-telegram-bot;
	pip install PyJWT;

setup:
	rm -rf sqlite3 words_explicit.db;
	mkdir tmp -p
	mkdir dataset -p && \
		cd dataset && \
		touch dictionary_es.txt;
	touch words_explicit.db;
	cat database/migrations/palabras.sql | sqlite3 words_explicit.db;

run:
	flask run -h 0.0.0.0 --port 5000

dev:
	flask --app app.py --debug run
