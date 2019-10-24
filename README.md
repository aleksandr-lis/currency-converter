## Currency Converter

```bash
git clone git@github.com:lis-space/currency-converter.git
cd currency-converter
echo "OER_APP_ID = 'YOURAPPID'" >> app/app/settings_local.py
./bin/up.sh
```

## API

Currencies list:
> http://0.0.0.0:8000/converter/currencies/

Rates list:
> http://0.0.0.0:8000/converter/rates/

Convert:
> http://0.0.0.0:8000/converter/CZK/PLN/100/

## Front

Converter
> http://0.0.0.0:3000/

## Tests

```bash
./bin/tests-app.sh
```

## License

MIT.
