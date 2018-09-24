# -*- coding: utf-8 -*-
import logging

from telegram import ChatAction, ChatMember, ParseMode

logger = logging.getLogger()


def pin(bot, update):
    logger.info("Command /pin received")

    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Emm... Qué mensaje debo anclar? (・・ ) ?")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_pin_messages and not chat_member.status == ChatMember.CREATOR:
        update.message.reply_sticker("CAADAgADoRsAAuCjggfsFEp1hLA7RQI")
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id, "Tú no puedes anclar mensajes")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_pin_messages:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("No tengo permisos para anclar mensajes (T_T)")
        return

    bot.pin_chat_message(update.message.chat.id, update.message.reply_to_message.message_id)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text("Anclado <(￣︶￣)>")


def pin_mute(bot, update):
    logger.info("Command /pinmute received")

    if update.message.reply_to_message is None:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("Emm... Qué mensaje debo anclar? (・・ ) ?")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if not chat_member.can_pin_messages and not chat_member.status == ChatMember.CREATOR:
        update.message.reply_sticker("CAADAgADoRsAAuCjggfsFEp1hLA7RQI")
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        bot.send_message(update.message.chat.id, "Tú no puedes anclar mensajes")
        return

    chat_member = bot.get_chat_member(update.message.chat.id, bot.get_me().id)
    if not chat_member.can_pin_messages:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("No tengo permisos para anclar mensajes (T_T)")
        return

    bot.pin_chat_message(update.message.chat.id, update.message.reply_to_message.message_id, True)

    bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
    update.message.reply_to_message.reply_text("Anclado <(￣︶￣)>")


def love(bot, update):
    logger.info("Command /love received")

    if update.message.from_user.id == 82982166:
        bot.send_chat_action(update.message.chat.id, ChatAction.TYPING)
        update.message.reply_text("La pareja más hermosa que he conocido son [Zoé](tg://user?id=359710858) y [Nahuel]" +
                                  "(tg://user?id=82982166) :3\n\nEsos dos tortolitos enamorados se aman " +
                                  "incondicionalmente, se acompañan en todo lo que pueden, y anteponen siempre las " +
                                  "necesidades del otro ❤️", ParseMode.MARKDOWN)
        bot.send_sticker(update.message.chat.id, "CAADAQADwQEAAuWyyh3shINoW9G1fwI")
