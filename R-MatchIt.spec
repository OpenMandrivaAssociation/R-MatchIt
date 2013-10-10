%global packname  MatchIt
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.4_21
Release:          1
Summary:          The skew-normal and skew-t distributions
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/MatchIt/index.html
Source0:          http://cran.r-project.org/src/contrib/MatchIt_2.4-21.tar.gz
BuildRequires:    R-devel R-MASS R-WhatIf R-cem R-nnet R-rpart R-mgcv R-Matching
Requires:         R-core R-MASS R-WhatIf R-cem R-nnet R-rpart R-mgcv R-Matching
BuildArch:        noarch

%description
Functions for manipulating skew-normal and skew-t probability distributions,
and for fitting them to data, in the scalar and in the multivariate case.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help