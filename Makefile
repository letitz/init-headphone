PROG=init-headphone
VERSION=0.2.0
SRCDIR=src
TARBALL=${PROG}-${VERSION}.tar.gz

all: pkg

pkg: ${TARBALL}

${TARBALL}: ${SRCDIR}/*
	tar -czf $@ $^

clean:
	rm -rf ${TARBALL}

