class MultiCommand:

    def split(self, command):

        text = command.lower()

        words = [
            " and ",
            " then ",
            " phir ",
            " fir ",
            ","
        ]

        commands = [text]

        for word in words:

            temp = []

            for cmd in commands:

                temp.extend(cmd.split(word))

            commands = temp

        return [x.strip() for x in commands if x.strip()]


multi = MultiCommand()