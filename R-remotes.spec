#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-remotes
Version  : 2.1.0
Release  : 15
URL      : https://cran.r-project.org/src/contrib/remotes_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/remotes_2.1.0.tar.gz
Summary  : R Package Installation from Remote Repositories, Including
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
# remotes
> Install R Packages from GitHub, BitBucket, or other local or remote
> repositories

%prep
%setup -q -c -n remotes

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561440186

%install
export SOURCE_DATE_EPOCH=1561440186
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library remotes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library remotes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library remotes
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc remotes || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/remotes/DESCRIPTION
/usr/lib64/R/library/remotes/INDEX
/usr/lib64/R/library/remotes/Meta/Rd.rds
/usr/lib64/R/library/remotes/Meta/features.rds
/usr/lib64/R/library/remotes/Meta/hsearch.rds
/usr/lib64/R/library/remotes/Meta/links.rds
/usr/lib64/R/library/remotes/Meta/nsInfo.rds
/usr/lib64/R/library/remotes/Meta/package.rds
/usr/lib64/R/library/remotes/Meta/vignette.rds
/usr/lib64/R/library/remotes/NAMESPACE
/usr/lib64/R/library/remotes/NEWS.md
/usr/lib64/R/library/remotes/R/remotes
/usr/lib64/R/library/remotes/R/remotes.rdb
/usr/lib64/R/library/remotes/R/remotes.rdx
/usr/lib64/R/library/remotes/doc/dependencies.Rmd
/usr/lib64/R/library/remotes/doc/dependencies.html
/usr/lib64/R/library/remotes/doc/index.html
/usr/lib64/R/library/remotes/help/AnIndex
/usr/lib64/R/library/remotes/help/aliases.rds
/usr/lib64/R/library/remotes/help/paths.rds
/usr/lib64/R/library/remotes/help/remotes.rdb
/usr/lib64/R/library/remotes/help/remotes.rdx
/usr/lib64/R/library/remotes/html/00Index.html
/usr/lib64/R/library/remotes/html/R.css
/usr/lib64/R/library/remotes/install-github.R
/usr/lib64/R/library/remotes/install-github.Rin
/usr/lib64/R/library/remotes/tests/testthat.R
/usr/lib64/R/library/remotes/tests/testthat/Biobase/DESCRIPTION
/usr/lib64/R/library/remotes/tests/testthat/MASS/DESCRIPTION
/usr/lib64/R/library/remotes/tests/testthat/archives/foo.tar
/usr/lib64/R/library/remotes/tests/testthat/archives/foo.tar.bz2
/usr/lib64/R/library/remotes/tests/testthat/archives/foo.tar.gz
/usr/lib64/R/library/remotes/tests/testthat/archives/foo.tbz
/usr/lib64/R/library/remotes/tests/testthat/archives/foo.tgz
/usr/lib64/R/library/remotes/tests/testthat/archives/foo.zip
/usr/lib64/R/library/remotes/tests/testthat/archives/foo/DESCRIPTION
/usr/lib64/R/library/remotes/tests/testthat/archives/foo/R/foo.R
/usr/lib64/R/library/remotes/tests/testthat/archives/foo/configure
/usr/lib64/R/library/remotes/tests/testthat/github-error-local.txt
/usr/lib64/R/library/remotes/tests/testthat/github-error-travis.txt
/usr/lib64/R/library/remotes/tests/testthat/helper.R
/usr/lib64/R/library/remotes/tests/testthat/invalidpkg/DESCRIPTION
/usr/lib64/R/library/remotes/tests/testthat/noremotes/DESCRIPTION
/usr/lib64/R/library/remotes/tests/testthat/submodule/DESCRIPTION
/usr/lib64/R/library/remotes/tests/testthat/submodule/NAMESPACE
/usr/lib64/R/library/remotes/tests/testthat/test-bioc.R
/usr/lib64/R/library/remotes/tests/testthat/test-cran.R
/usr/lib64/R/library/remotes/tests/testthat/test-dcf.R
/usr/lib64/R/library/remotes/tests/testthat/test-decompress.R
/usr/lib64/R/library/remotes/tests/testthat/test-deps.R
/usr/lib64/R/library/remotes/tests/testthat/test-devel.R
/usr/lib64/R/library/remotes/tests/testthat/test-download.R
/usr/lib64/R/library/remotes/tests/testthat/test-git.R
/usr/lib64/R/library/remotes/tests/testthat/test-github.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-bioc.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-bitbucket.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-cran.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-deps.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-dev.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-git.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-github.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-gitlab.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-local.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-remote.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-svn.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-url.R
/usr/lib64/R/library/remotes/tests/testthat/test-install-version.R
/usr/lib64/R/library/remotes/tests/testthat/test-install.R
/usr/lib64/R/library/remotes/tests/testthat/test-json.R
/usr/lib64/R/library/remotes/tests/testthat/test-package-deps.R
/usr/lib64/R/library/remotes/tests/testthat/test-package.R
/usr/lib64/R/library/remotes/tests/testthat/test-parse-git.R
/usr/lib64/R/library/remotes/tests/testthat/test-script.R
/usr/lib64/R/library/remotes/tests/testthat/test-submodule.R
/usr/lib64/R/library/remotes/tests/testthat/test-system.R
/usr/lib64/R/library/remotes/tests/testthat/test-utils.R
/usr/lib64/R/library/remotes/tests/testthat/withremotes/DESCRIPTION
