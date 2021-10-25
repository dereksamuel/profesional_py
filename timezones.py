from datetime import datetime;
import pytz;


bogota_timezone = pytz.timezone("America/Bogota");
bogota_datetime = datetime.now(bogota_timezone);
print("Bogota: ", bogota_datetime.strftime("%d/%m/%Y, %Hh:%Mm:%Ss"));


mexico_timezone = pytz.timezone("America/Mexico_City");
mexico_datetime = datetime.now(mexico_timezone);
print("Mexico: ", mexico_datetime.strftime("%d/%m/%Y, %H:%M:%S"));


caracas_timezone = pytz.timezone("America/Caracas");
caracas_datetime = datetime.now(caracas_timezone);
print("caracas: ", caracas_datetime.strftime("%d/%m/%Y, %H:%M:%S"));

