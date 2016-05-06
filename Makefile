SBINDIR=/usr/sbin
SYSCONFDIR=/etc
UNITDIR=/usr/lib/systemd/system

all:

install:
	install -Dm 755 init-headphone ${DESTDIR}${SBINDIR}/init-headphone
	install -Dm 755 init-headphone.conf ${DESTDIR}${SYSCONFDIR}/modules-load.d/init-headphone.conf
	install -Dm 755 init-headphone.service ${DESTDIR}${UNITDIR}/init-headphone.service

