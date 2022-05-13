# Password Education

**Related information**  


[Passwords](passwords.md)

## liverpool, monkey, chocolate

What a strange title for an article. These words are all in the top 20 most common passwords used in the UK in 2020. The number 1 most common password, both globally and in the UK, is `123456`. The passwords in the title are the 3rd most common UK password \(`liverpool`\), the 15th \(`monkey`\), and the 18th \(`chocolate`\).

The list they appear on comes out every year and is based on research by independent cybersecurity incident researchers. These are all passwords that were exposed in 2020. They are ranked based on how many times they appear. There are lots of lists like this on the internet, with lots of common passwords on. Hackers use them to add to their password dictionaries.

![Screenshot from the Nordpass password list 2020. This is a list of the findings for the UK. It lists the top 9 ranked passwords used, the time taken to crack them, and the count for each password. The number 1 password is 123456; it takes less than 1 second to crack. Number 2 is password; it takes less than 1 second to crack. Number 3 is liverpool; it takes less than 1 second to crack. Number 4 is password1; it takes less than 1 second to crack. Number 5 is 123456789; it takes less than 1 second to crack. Number 6 is 12345; it takes less than 1 second to crack. Number 7 is qwerty; it takes less than 1 second to crack. Number 8 is liverpool1; it takes less than 1 second to crack. Lastly, number 9 is charlie; it takes less than 1 second to crack.](images/nordpass2020.png)

[Screenshot from NordPass password list 2020](https://nordpass.com/most-common-passwords-list/)

These dictionaries are used to guess people's passwords. This is called password cracking. The dictionary lists often have hundreds of thousands of words and passwords in. They include common formulas that people use to create passwords; things like `Spring2022!` that changes to `Summer2022!` then `Autumn2022!`, or the name of something at work with a number at the end that is changed every so often, like `Justice123`. Formulaic passwords like this are very easy to guess.

Hackers also use rules to help them guess common password formulas. These allow for multiple versions of each guess to try commonly used password making techniques. They include substitutions for letters and adding numbers and symbols to the end.

![Image showing different rules that can be used. The first rule is 'add a number at the end', then there is an image of a key, then a box with 'monkey1, monkey2, monkey3, ..., monkey9' in one column and 'monkey001, monkey002, monkey003, ..., monkey999' in the second column. The next rule is 'add a special character at the end', then there is an image of a key, then there is a box with 'monkey!, chocolate!, liverpool! in one column and 'monkey$, monkey&, monkey% in the second column. The final rule is 'substitute a letter for a number or special character', then there is an image of a key, then a box with 'monkey, m0nkey, monk3y, m0nk3y' in one column and 'password, p4$$word, p@55w0rd, p@$5w0rd' in the second column.](images/hacker-password-rules.png)

Examples of rules used by hackers in a dictionary list.

But it must take ages to run through hundreds of thousands of words to crack your password, surely? Not at all. Remember those three passwords in the title of this article? They take less than 1 second to crack. Computers can make billions of guesses every second. The more common a password is, the easier it is to crack. The shorter a password is, the easier it is to crack.

> When it comes to passwords complexity is not strength.

> Length is Strength.

## Some password maths

For each character in a password, there are 94 possible choices:

> 26 upper case letters + 26 lower case letters + 32 special characters + 10 numbers = 94 possible characters

Computers are so powerful now that they can crack a short password almost instantly. Every additional character used increases the potential combinations exponentially.

To work out how many combinations are possible for your password you multiply 94 to the power of how many characters are in your password.

![Image showing the title 'Maths' and a icon image of a calculator to the right. The words in the image read: 94^8 for 8 character password = 6,095,689,385,410,816. The next calculation is 94^20 for 20 character password = 2,901,062,411,314,618,233,730,627,546,741,369,470,976.](images/maths.png)

Image showing the maths involved when calculating the possible combinations of characters in a password.

Compare the 8 character password possible combinations to the 20 character password possible combinations. It could take a computer under an hour to crack an 8 character password. A [TechRepublic article](https://www.techrepublic.com/article/how-an-8-character-password-could-be-cracked-in-less-than-an-hour/) shows how fast computers can crack passwords. However, it would take an unreasonably long time to crack a 20 character password. That would take billions of years.

## What makes a bad password?

Bad passwords often have one or more of these characteristics:

-   They are short.
-   They use an easy to guess formula, for example changing a season or a month or adding a number to the end.
-   They use special characters at the end, for example `!`
-   They use a common word or combination of numbers that lots of other people use, for example `123456`.

There are popular formulas and patterns as well:

-   `qwertyuiop` is the 25th most common password globally.
-   `1q2w3e4r` is the 47th most common password globally.
-   `789456123` is the 100th most common password globally.

These can all be cracked in under 1 second.

Complex random passwords are very hard for people to remember. A short password, no matter how complex, is easy to crack. Remember:

> Complexity is not strength

## How can you make a good password?

When it comes to passwords:

> Length is Strength.

Use three or four random words to create a passphrase that is easy to remember and very strong.

Flip through a dictionary or use an online random word generator to collect a few random words. Put them together in a way that you will be able to remember - maybe it makes you laugh. Once you have a long password, you can make it complex by adding numbers and special characters between the words.

Some examples of putting three or four random words together to make very strong and hard to crack passwords are:

-   `TractorBandage8Snake`
-   `GreenDuck9Burgerrooftop`
-   `fortunegreenhouseelephantsunflower`
-   `custard!porridge4RailwayChicken`

## Things to avoid when making a password

It is really important when picking your random words that they aren't connected to you, your family, your pets, or your workplace. Don't use names of friends or important dates like birthdays or weddings. Hackers can look at data online about you and your connections to discover things like your favourite food or musician, your pet's name or breed, and other things it is tempting to use in a password. Avoid using lyrics and quotes as those will also be in that big dictionary list used for cracking passwords.

Always use a unique password for every account you have.

## Multi-factor authentication

[Multi-factor authentication \(MFA\)](Multi-factor authentication (MFA)phishing-guide.dita/#multi-factor-authentication-mfa), also called two factor authentication \(2FA\), is a great way to add extra security to your accounts. This requires you to enter a code after entering your password. No-one will ever ask you for this code. You should be the only one entering the MFA code. You should only enter the MFA code if you are actively logging in to your account yourself. If a hacker does manage to crack your password, they won't have your MFA code, so they won't be able to access your account.

Password managers are a great way to store all your passwords safely. They remember your passwords for you. Make sure you have a strong password to login to the password manager. Remember:

> Length is Strength.

Password managers can also suggest long and strong passwords for you. You can write passwords down in a password book, but make sure you store this away from your computer. If you travel with your laptop, never keep your password book in the same bag in case your laptop bag gets stolen. This way the thief won't also have your passwords. If you use a password book in an office, keep it locked away when not in use. Never create a digital file with your passwords in.

## Recap

Short passwords are easy for hackers to guess. Short passwords - no matter how complex - are easy to crack. Complexity is not strength. Use 3 or 4 random words to create a long strong password. Remember:

> Length is Strength.

You can add complexity once you have a long password by putting numbers or special characters between your random words.

We have a [very short micro survey](https://forms.office.com/r/Q4Ck9d8vXC) where you get to rate the strength of passwords. It takes less than two minutes!

![A thumbnail of the strong password information poster.](images/how-to-make-strong-passwords.png)

A useful information leaflet on strong passwords is available for download [here](./culture/how-to-make-strong-passwords.pdf).

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

