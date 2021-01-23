import java.time.Duration;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZoneOffset;

class Gigasecond {
	private static final Duration GIGA_SECOND = Duration.ofSeconds(1_000_000_000L);
    private LocalDateTime date;
    
    Gigasecond(LocalDate moment) {
    	this(moment.atStartOfDay());
    }

    Gigasecond(LocalDateTime moment) {
    	date = moment.plus(GIGA_SECOND);
    }
    
    LocalDateTime getDateTime() { 
        return date;
    }

}
