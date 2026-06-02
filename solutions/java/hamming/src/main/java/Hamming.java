class Hamming {
    private final String leftStrand;
    private final String rightStrand;

    Hamming(final String leftStrand, final String rightStrand) {
        checkStrandsNotEmpty(leftStrand, rightStrand);
        checkStrandsEqualLength(leftStrand, rightStrand);
        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
    }

    int getHammingDistance() {
        int hammingDistance = 0;

        for (int i = 0; i < leftStrand.length(); i++) {
            if (leftStrand.charAt(i) != rightStrand.charAt(i)) {
                hammingDistance++;
            }
        }

        return hammingDistance;
    }

    private void checkStrandsNotEmpty(final String left, final String right) {

        if (left.length() == right.length()) {
            return;
        }

        if (left.isEmpty()) {
            throwStringEmptyException("left");
        }

        if (right.isEmpty()) {
            throwStringEmptyException("right");
        }
    }

    private void throwStringEmptyException(final String sideEmpty) {
        final String lengthExpMessage = String.format("%s strand must not be empty.", sideEmpty);
        throw new IllegalArgumentException(lengthExpMessage);
    }

    private void checkStrandsEqualLength(final String left, final String right) {
        if (left.length() != right.length()) {
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
        }
    }

}
