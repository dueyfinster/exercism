import java.util.Optional;

class Twofer {
    private static final String twoFer = "One for %s, one for me.";

    String twofer(final String name) {
        final String newName = Optional.ofNullable(name).orElse("you");

        return String.format(twoFer, newName);
    }
}
