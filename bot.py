import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# ======================
# CONFIGURATION
# ======================

BOT_TOKEN = "8420081070:AAGSc0FKAz9Gy7RPJlXcjxa3PdJLqHyoiz0"
ADMIN_USERNAME = "@escoadmin1"

# Each image filename MUST match exactly what is inside the proofs folder
PROOF_CAPTIONS = {
    "proof1.jpg": (
        "✅ *REVIEWED PRODUCT:* Paypal Flip\n"
        "💰 Successful payment received\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof2.jpg": (
        "✅ *REVIEWED PRODUCT:* Fake Money\n"
        "💰 Funds deliverded successfully\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof3.jpg": (
        "✅ *REVIEWED PRODUCT:* Clone Card and Withdrawal\n"
        "💰 Money withdrawal confirmed\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof4.jpg": (
        "✅ *REVIEWED PRODUCT:* Paypal Flip\n"
        "💰 Successful payment\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof5.jpg": (
        "✅ *REVIEWED PRODUCT:* Paypal Flip\n"
        "💰 Successful payment received\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof6.jpg": (
        "✅ *REVIEWED PRODUCT:* Paypal Flip\n"
        "💰 Successful payment received\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof7.jpg": (
        "✅ *REVIEWED PRODUCT:* Paypal Flip\n"
        "💰 Successful payment received\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof8.jpg": (
        "✅ *REVIEWED PRODUCT:* Paypal Flip\n"
        "💰 Successful payment received\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof9.jpg": (
        "✅ *REVIEWED PRODUCT:* Fake Money\n"
        "💰 Funds deliverded successfully\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),

    "proof10.jpg": (
        "✅*REVIEWED PRODUCT:* Fake Money\n"
        "💰 Funds deliverded successfully\n\n"
        "👑 *ADMIN:* @escoadmin1"
    ),
}

# ======================
# /start COMMAND
# ======================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👑 OUR ONLY ADMIN 👑", callback_data="admin")],
        [InlineKeyboardButton("✨ VIEW PROOFS ✨", callback_data="proofs")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔹 *Main Menu*\n\nChoose an option below 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# ======================
# BUTTON HANDLER
# ======================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ADMIN BUTTON
    if query.data == "admin":
        await query.message.reply_text(
            f"👑 *OUR ONLY ADMIN*\n\n{ADMIN_USERNAME}",
            parse_mode="Markdown"
        )

    # VIEW PROOFS BUTTON
    elif query.data == "proofs":
        proof_folder = "proofs"

        # Check if folder exists
        if not os.path.exists(proof_folder):
            await query.message.reply_text("❌ No proofs available yet.")
            return

        images = sorted(os.listdir(proof_folder))

        # Check if folder is empty
        if not images:
            await query.message.reply_text("❌ No proofs found.")
            return

        # Send each image with its own caption
        for img in images:
            img_path = os.path.join(proof_folder, img)

            caption = PROOF_CAPTIONS.get(
                img,
                f"👑 *ADMIN:* {ADMIN_USERNAME}"
            )

            with open(img_path, "rb") as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption=caption,
                    parse_mode="Markdown"
                )

# ======================
# MAIN FUNCTION
# ======================

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
