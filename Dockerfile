# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Kyy-Userbot ━━━━━━

RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y
RUN git clone -b testi https://github.com/muhammadrizky16/Kyy-Userbot /root/userbot
RUN /bin/sh -c curl https://raw.githubusercontent.com/creationix/nvm/v0.30.1/install.sh | bash     && . $NVM_DIR/nvm.sh     && nvm install $NODE_VERSION     && nvm alias default $NODE_VERSION     && nvm use default # buildkit
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/muhammadrizky16/Kyy-Userbot/testi/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
