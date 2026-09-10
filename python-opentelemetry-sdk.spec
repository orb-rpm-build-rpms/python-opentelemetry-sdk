Name:           python-opentelemetry-sdk
# Aligned to the base opentelemetry-api (1.39.1) rather than the latest 1.44.0:
# the SDK pins opentelemetry-api and opentelemetry-semantic-conventions to its
# exact version, so 1.44.0 would force rebuilding api too. 1.39.1 reuses the
# base api and pairs with semantic-conventions 0.60b1. vLLM only needs >=1.27.0.
Version:        1.39.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenTelemetry Python SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-sdk
Source:         %{pypi_source opentelemetry_sdk}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-sdk' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-opentelemetry-sdk
Summary:        %{summary}

%description -n python3-opentelemetry-sdk %_description

# The file-configuration extra (present in 1.44.0) does not exist in 1.39.1, and
# vLLM does not need it, so no extras are packaged.


%prep
%autosetup -p1 -n opentelemetry_sdk-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l opentelemetry


%check
%pyproject_check_import


%files -n python3-opentelemetry-sdk -f %{pyproject_files}


%changelog
%autochangelog
