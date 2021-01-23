import java.util.List;
import java.util.stream.Collectors;

class Scrabble {
	private int score = 0;
	
    Scrabble(String word) {
    	final char[] chars = word.toCharArray();
		calculateWordScore(chars);
    }
    
    private void calculateWordScore(final char[] chars) {
    	for(char c : chars) {
    		score = score + letterScores(c);
    	}
    }

    int getScore() {
    	return score;
    }

    private int letterScores(char letter) {
    	letter = Character.toUpperCase(letter);
    	switch(letter) {
    		case 'A':
    		case 'E':
    		case 'I':
    		case 'O':
    		case 'U':
    		case 'L':
    		case 'N':
    		case 'R':
    		case 'S':
    		case 'T':
    			return 1;
    		case 'D':
    		case 'G':
    			return 2;
    		case 'B':
    		case 'C':
    		case 'M':
    		case 'P':
    			return 3;
    		case 'F':
    		case 'H':
    		case 'V':
    		case 'W':
    		case 'Y':
    			return 4;
    		case 'K':
    			return 5;
    		case 'J':
    		case 'X':
    			return 8;
    		case 'Q':
    		case 'Z':
    			return 10;
    		default:
    			return 0;
    	}
    }
}
