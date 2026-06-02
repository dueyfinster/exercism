import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Acronym {
	private final String phrase;
	private String acronym;
	private final Pattern pattern = Pattern.compile("[A-Za-z']+"); // pattern to match words

    Acronym(String phrase) {
    	this.phrase = phrase.toUpperCase();
    	calculateAcronym();
    }
    
    private void calculateAcronym() {
    	final Matcher matcher = pattern.matcher(this.phrase);
    	final char[] p1 = this.phrase.toCharArray();
    	final StringBuffer sb = new StringBuffer();

        while (matcher.find()) {
            sb.append(p1[matcher.start()]); // Get start of match (first letter)
        }
        
        this.acronym = sb.toString();
    }

    String get() {
        return this.acronym;
    }

}
