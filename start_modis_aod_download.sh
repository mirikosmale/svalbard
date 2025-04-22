#!/bin/bash

GREP_OPTIONS=''

cookiejar=$(mktemp cookies.XXXXXXXXXX)
netrc=$(mktemp netrc.XXXXXXXXXX)
chmod 0600 "$cookiejar" "$netrc"
function finish {
  rm -rf "$cookiejar" "$netrc"
}

trap finish EXIT
WGETRC="$wgetrc"

prompt_credentials() {
    echo "Enter your Earthdata Login or other provider supplied credentials"
    read -p "Username (mirikosmale): " username
    username=${username:-mirikosmale}
    read -s -p "Password: " password
    echo "machine urs.earthdata.nasa.gov login $username password $password" >> $netrc
    echo
}

exit_with_error() {
    echo
    echo "Unable to Retrieve Data"
    echo
    echo $1
    echo
    echo "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024118.h18v01.061.2024120034737/MCD19A2.A2024118.h18v01.061.2024120034737.hdf"
    echo
    exit 1
}

prompt_credentials
  detect_app_approval() {
    approved=`curl -s -b "$cookiejar" -c "$cookiejar" -L --max-redirs 5 --netrc-file "$netrc" https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024118.h18v01.061.2024120034737/MCD19A2.A2024118.h18v01.061.2024120034737.hdf -w '\n%{http_code}' | tail  -1`
    if [ "$approved" -ne "200" ] && [ "$approved" -ne "301" ] && [ "$approved" -ne "302" ]; then
        # User didn't approve the app. Direct users to approve the app in URS
        exit_with_error "Please ensure that you have authorized the remote application by visiting the link below "
    fi
}

setup_auth_curl() {
    # Firstly, check if it require URS authentication
    status=$(curl -s -z "$(date)" -w '\n%{http_code}' https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024118.h18v01.061.2024120034737/MCD19A2.A2024118.h18v01.061.2024120034737.hdf | tail -1)
    if [[ "$status" -ne "200" && "$status" -ne "304" ]]; then
        # URS authentication is required. Now further check if the application/remote service is approved.
        detect_app_approval
    fi
}

setup_auth_wget() {
    # The safest way to auth via curl is netrc. Note: there's no checking or feedback
    # if login is unsuccessful
    touch ~/.netrc
    chmod 0600 ~/.netrc
    credentials=$(grep 'machine urs.earthdata.nasa.gov' ~/.netrc)
    if [ -z "$credentials" ]; then
        cat "$netrc" >> ~/.netrc
    fi
}

fetch_urls() {
  if command -v curl >/dev/null 2>&1; then
      setup_auth_curl
      while read -r line; do
        # Get everything after the last '/'
        filename="${line##*/}"

        # Strip everything after '?'
        stripped_query_params="${filename%%\?*}"

        curl -f -b "$cookiejar" -c "$cookiejar" -L --netrc-file "$netrc" -g -o $stripped_query_params -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
      done;
  elif command -v wget >/dev/null 2>&1; then
      # We can't use wget to poke provider server to get info whether or not URS was integrated without download at least one of the files.
      echo
      echo "WARNING: Can't find curl, use wget instead."
      echo "WARNING: Script may not correctly identify Earthdata Login integrations."
      echo
      setup_auth_wget
      while read -r line; do
        # Get everything after the last '/'
        filename="${line##*/}"

        # Strip everything after '?'
        stripped_query_params="${filename%%\?*}"

        wget --load-cookies "$cookiejar" --save-cookies "$cookiejar" --output-document $stripped_query_params --keep-session-cookies -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
      done;
  else
      exit_with_error "Error: Could not find a command-line downloader.  Please install curl or wget"
  fi
}

fetch_urls <<'EDSCEOF'
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024118.h18v01.061.2024120034737/MCD19A2.A2024118.h18v01.061.2024120034737.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024118.h18v00.061.2024120034848/MCD19A2.A2024118.h18v00.061.2024120034848.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024118.h17v00.061.2024120035411/MCD19A2.A2024118.h17v00.061.2024120035411.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024117.h18v00.061.2024118234605/MCD19A2.A2024117.h18v00.061.2024118234605.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024117.h17v00.061.2024118235205/MCD19A2.A2024117.h17v00.061.2024118235205.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024117.h18v01.061.2024118235123/MCD19A2.A2024117.h18v01.061.2024118235123.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024116.h18v01.061.2024117174113/MCD19A2.A2024116.h18v01.061.2024117174113.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024116.h17v00.061.2024117175100/MCD19A2.A2024116.h17v00.061.2024117175100.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024116.h18v00.061.2024117175345/MCD19A2.A2024116.h18v00.061.2024117175345.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024115.h17v00.061.2024117021934/MCD19A2.A2024115.h17v00.061.2024117021934.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024115.h18v01.061.2024117024455/MCD19A2.A2024115.h18v01.061.2024117024455.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024115.h18v00.061.2024117021024/MCD19A2.A2024115.h18v00.061.2024117021024.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024114.h18v00.061.2024116010730/MCD19A2.A2024114.h18v00.061.2024116010730.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024114.h17v00.061.2024116011239/MCD19A2.A2024114.h17v00.061.2024116011239.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024114.h18v01.061.2024116010608/MCD19A2.A2024114.h18v01.061.2024116010608.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024113.h18v00.061.2024115191324/MCD19A2.A2024113.h18v00.061.2024115191324.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024113.h17v00.061.2024115180057/MCD19A2.A2024113.h17v00.061.2024115180057.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024113.h18v01.061.2024115175705/MCD19A2.A2024113.h18v01.061.2024115175705.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024112.h17v00.061.2024115161515/MCD19A2.A2024112.h17v00.061.2024115161515.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024112.h18v01.061.2024115162019/MCD19A2.A2024112.h18v01.061.2024115162019.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024112.h18v00.061.2024115162723/MCD19A2.A2024112.h18v00.061.2024115162723.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024111.h17v00.061.2024115095109/MCD19A2.A2024111.h17v00.061.2024115095109.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024111.h18v01.061.2024115094133/MCD19A2.A2024111.h18v01.061.2024115094133.hdf
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/MCD19A2.061/MCD19A2.A2024111.h18v00.061.2024115091648/MCD19A2.A2024111.h18v00.061.2024115091648.hdf
EDSCEOF
